# EMA Hourly Continuation — IO/USDT P8_144

**Symbol:** IO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.7820 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.8927 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -1.4558 |
| sortino_ratio | -0.3837 |
| max_drawdown | 0.3988 |
| cagr | -0.1631 |
| net_avg_win | 80.8904 |
| net_avg_loss | -91.9521 |
| avg_hold_time_bars | 47.5108 |
| exposure | 0.7429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
