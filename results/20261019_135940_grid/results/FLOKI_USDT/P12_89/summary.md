# EMA Hourly Continuation — FLOKI/USDT P12_89

**Symbol:** FLOKI/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 724 |
| net_profit_factor | 0.6466 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.9322 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -4.0253 |
| sortino_ratio | -1.5207 |
| max_drawdown | 0.8475 |
| cagr | -0.5177 |
| net_avg_win | 44.6745 |
| net_avg_loss | -62.5421 |
| avg_hold_time_bars | 16.6782 |
| exposure | 0.5489 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
