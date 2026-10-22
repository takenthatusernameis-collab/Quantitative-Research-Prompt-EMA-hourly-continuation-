# EMA Hourly Continuation — XAI/USDT P89_144

**Symbol:** XAI/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.7618 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 0.9827 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -1.5398 |
| sortino_ratio | -0.3767 |
| max_drawdown | 0.4022 |
| cagr | -0.1595 |
| net_avg_win | 78.5403 |
| net_avg_loss | -100.3090 |
| avg_hold_time_bars | 9.0171 |
| exposure | 0.1197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
