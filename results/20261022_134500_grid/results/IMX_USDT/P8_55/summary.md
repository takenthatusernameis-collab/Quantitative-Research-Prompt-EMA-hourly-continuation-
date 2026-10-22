# EMA Hourly Continuation — IMX/USDT P8_55

**Symbol:** IMX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 966 |
| net_profit_factor | 0.6874 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 1.0327 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -3.8661 |
| sortino_ratio | -1.6902 |
| max_drawdown | 0.8779 |
| cagr | -0.5531 |
| net_avg_win | 39.8076 |
| net_avg_loss | -57.1952 |
| avg_hold_time_bars | 11.2153 |
| exposure | 0.4902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
