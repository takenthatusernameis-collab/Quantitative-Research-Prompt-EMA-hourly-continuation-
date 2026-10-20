# EMA Hourly Continuation — ONE/USDT P55_144

**Symbol:** ONE/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.6891 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 1.0027 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -2.8023 |
| sortino_ratio | -0.8484 |
| max_drawdown | 0.6497 |
| cagr | -0.3287 |
| net_avg_win | 64.0033 |
| net_avg_loss | -85.8274 |
| avg_hold_time_bars | 13.3289 |
| exposure | 0.2763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
