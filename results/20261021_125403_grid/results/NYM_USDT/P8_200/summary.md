# EMA Hourly Continuation — NYM/USDT P8_200

**Symbol:** NYM/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.4905 |
| net_win_rate | 0.3851 |
| gross_profit_factor | 0.6452 |
| gross_win_rate | 0.3882 |
| sharpe_ratio | -3.9956 |
| sortino_ratio | -1.0079 |
| max_drawdown | 0.6988 |
| cagr | -0.3749 |
| net_avg_win | 53.7676 |
| net_avg_loss | -68.6548 |
| avg_hold_time_bars | 50.9099 |
| exposure | 0.7451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
