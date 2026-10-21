# EMA Hourly Continuation — DAG/USDT P12_200

**Symbol:** DAG/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.8273 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9474 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -1.0540 |
| sortino_ratio | -0.2829 |
| max_drawdown | 0.3666 |
| cagr | -0.1240 |
| net_avg_win | 78.3064 |
| net_avg_loss | -90.4693 |
| avg_hold_time_bars | 39.0960 |
| exposure | 0.6291 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
