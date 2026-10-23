# EMA Hourly Continuation — XAI/USDT P26_89

**Symbol:** XAI/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 724 |
| net_profit_factor | 0.6731 |
| net_win_rate | 0.4682 |
| gross_profit_factor | 0.9699 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -4.3637 |
| sortino_ratio | -1.6581 |
| max_drawdown | 0.8738 |
| cagr | -0.5447 |
| net_avg_win | 52.3217 |
| net_avg_loss | -68.4436 |
| avg_hold_time_bars | 11.0787 |
| exposure | 0.3646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
