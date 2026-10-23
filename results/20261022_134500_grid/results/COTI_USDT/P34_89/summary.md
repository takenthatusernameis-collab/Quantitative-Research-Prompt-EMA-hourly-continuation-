# EMA Hourly Continuation — COTI/USDT P34_89

**Symbol:** COTI/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 758 |
| net_profit_factor | 0.5960 |
| net_win_rate | 0.4776 |
| gross_profit_factor | 0.9173 |
| gross_win_rate | 0.4842 |
| sharpe_ratio | -4.3795 |
| sortino_ratio | -1.7002 |
| max_drawdown | 0.8740 |
| cagr | -0.5575 |
| net_avg_win | 35.4982 |
| net_avg_loss | -54.4432 |
| avg_hold_time_bars | 6.4182 |
| exposure | 0.2211 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
