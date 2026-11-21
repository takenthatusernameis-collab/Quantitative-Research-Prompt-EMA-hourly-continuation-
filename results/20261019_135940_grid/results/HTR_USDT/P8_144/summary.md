# EMA Hourly Continuation — HTR/USDT P8_144

**Symbol:** HTR/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 760 |
| net_profit_factor | 0.4997 |
| net_win_rate | 0.3882 |
| gross_profit_factor | 0.6888 |
| gross_win_rate | 0.3961 |
| sharpe_ratio | -6.8874 |
| sortino_ratio | -2.6590 |
| max_drawdown | 0.9607 |
| cagr | -0.7232 |
| net_avg_win | 32.5069 |
| net_avg_loss | -41.2734 |
| avg_hold_time_bars | 18.4987 |
| exposure | 0.6390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
