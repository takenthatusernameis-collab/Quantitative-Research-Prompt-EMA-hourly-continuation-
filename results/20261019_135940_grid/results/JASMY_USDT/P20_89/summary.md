# EMA Hourly Continuation — JASMY/USDT P20_89

**Symbol:** JASMY/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 753 |
| net_profit_factor | 0.7113 |
| net_win_rate | 0.5139 |
| gross_profit_factor | 1.0565 |
| gross_win_rate | 0.5193 |
| sharpe_ratio | -2.9163 |
| sortino_ratio | -1.1321 |
| max_drawdown | 0.7640 |
| cagr | -0.4160 |
| net_avg_win | 47.1775 |
| net_avg_loss | -70.1273 |
| avg_hold_time_bars | 10.3519 |
| exposure | 0.3543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
