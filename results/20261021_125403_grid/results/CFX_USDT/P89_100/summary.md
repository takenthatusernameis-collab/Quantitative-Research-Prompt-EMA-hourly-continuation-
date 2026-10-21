# EMA Hourly Continuation — CFX/USDT P89_100

**Symbol:** CFX/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 116 |
| net_profit_factor | 0.6837 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 0.9629 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -1.2645 |
| sortino_ratio | -0.1955 |
| max_drawdown | 0.2006 |
| cagr | -0.0853 |
| net_avg_win | 76.0589 |
| net_avg_loss | -107.4771 |
| avg_hold_time_bars | 4.5259 |
| exposure | 0.0239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
