# EMA Hourly Continuation — XAI/USDT P89_200

**Symbol:** XAI/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.8844 |
| net_win_rate | 0.5226 |
| gross_profit_factor | 1.0920 |
| gross_win_rate | 0.5226 |
| sharpe_ratio | -0.6084 |
| sortino_ratio | -0.1429 |
| max_drawdown | 0.2407 |
| cagr | -0.0659 |
| net_avg_win | 86.6156 |
| net_avg_loss | -107.1927 |
| avg_hold_time_bars | 18.1955 |
| exposure | 0.2200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
