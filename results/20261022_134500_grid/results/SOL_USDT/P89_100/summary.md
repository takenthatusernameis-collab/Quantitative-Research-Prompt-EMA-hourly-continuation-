# EMA Hourly Continuation — SOL/USDT P89_100

**Symbol:** SOL/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 579 |
| net_profit_factor | 0.1872 |
| net_win_rate | 0.3299 |
| gross_profit_factor | 0.6880 |
| gross_win_rate | 0.4024 |
| sharpe_ratio | -11.3295 |
| sortino_ratio | -4.1037 |
| max_drawdown | 0.9969 |
| cagr | -0.8995 |
| net_avg_win | 12.0234 |
| net_avg_loss | -31.6116 |
| avg_hold_time_bars | 1.7807 |
| exposure | 0.0469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
