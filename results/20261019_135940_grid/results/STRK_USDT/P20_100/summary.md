# EMA Hourly Continuation — STRK/USDT P20_100

**Symbol:** STRK/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.6814 |
| net_win_rate | 0.4835 |
| gross_profit_factor | 0.9748 |
| gross_win_rate | 0.4849 |
| sharpe_ratio | -3.5696 |
| sortino_ratio | -1.3316 |
| max_drawdown | 0.8071 |
| cagr | -0.4670 |
| net_avg_win | 50.5472 |
| net_avg_loss | -69.4285 |
| avg_hold_time_bars | 12.3554 |
| exposure | 0.3903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
