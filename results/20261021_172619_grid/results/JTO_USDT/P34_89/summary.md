# EMA Hourly Continuation — JTO/USDT P34_89

**Symbol:** JTO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.7626 |
| net_win_rate | 0.4809 |
| gross_profit_factor | 0.9388 |
| gross_win_rate | 0.4809 |
| sharpe_ratio | -1.8693 |
| sortino_ratio | -0.5628 |
| max_drawdown | 0.5411 |
| cagr | -0.2278 |
| net_avg_win | 71.6728 |
| net_avg_loss | -87.0680 |
| avg_hold_time_bars | 10.5393 |
| exposure | 0.2132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
