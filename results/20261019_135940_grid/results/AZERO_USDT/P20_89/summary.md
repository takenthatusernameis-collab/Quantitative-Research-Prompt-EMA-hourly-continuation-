# EMA Hourly Continuation — AZERO/USDT P20_89

**Symbol:** AZERO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.5852 |
| net_win_rate | 0.4580 |
| gross_profit_factor | 0.9214 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -4.0371 |
| sortino_ratio | -1.4560 |
| max_drawdown | 0.8402 |
| cagr | -0.5027 |
| net_avg_win | 38.3096 |
| net_avg_loss | -55.3134 |
| avg_hold_time_bars | 13.2823 |
| exposure | 0.4003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
