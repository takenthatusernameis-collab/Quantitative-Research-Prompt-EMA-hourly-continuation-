# EMA Hourly Continuation — JASMY/USDT P50_200

**Symbol:** JASMY/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.9798 |
| net_win_rate | 0.5736 |
| gross_profit_factor | 1.3325 |
| gross_win_rate | 0.5736 |
| sharpe_ratio | -0.0535 |
| sortino_ratio | -0.0140 |
| max_drawdown | 0.1898 |
| cagr | -0.0131 |
| net_avg_win | 82.7496 |
| net_avg_loss | -113.5944 |
| avg_hold_time_bars | 28.1171 |
| exposure | 0.4256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
