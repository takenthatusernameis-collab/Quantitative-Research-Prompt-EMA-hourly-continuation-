# EMA Hourly Continuation — TFUEL/USDT P26_89

**Symbol:** TFUEL/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 851 |
| net_profit_factor | 0.4696 |
| net_win_rate | 0.4066 |
| gross_profit_factor | 0.7665 |
| gross_win_rate | 0.4136 |
| sharpe_ratio | -7.8398 |
| sortino_ratio | -3.2043 |
| max_drawdown | 0.9819 |
| cagr | -0.7927 |
| net_avg_win | 25.1021 |
| net_avg_loss | -36.6267 |
| avg_hold_time_bars | 7.6498 |
| exposure | 0.2946 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
