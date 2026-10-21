# EMA Hourly Continuation — CHR/USDT P20_200

**Symbol:** CHR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.9119 |
| net_win_rate | 0.5138 |
| gross_profit_factor | 1.0534 |
| gross_win_rate | 0.5138 |
| sharpe_ratio | -0.4302 |
| sortino_ratio | -0.0981 |
| max_drawdown | 0.2899 |
| cagr | -0.0471 |
| net_avg_win | 91.2498 |
| net_avg_loss | -105.7654 |
| avg_hold_time_bars | 61.9209 |
| exposure | 0.7089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
