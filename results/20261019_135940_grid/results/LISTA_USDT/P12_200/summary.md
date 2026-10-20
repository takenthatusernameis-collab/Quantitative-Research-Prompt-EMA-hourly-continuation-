# EMA Hourly Continuation — LISTA/USDT P12_200

**Symbol:** LISTA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.7704 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0212 |
| gross_win_rate | 0.5095 |
| sharpe_ratio | -1.7151 |
| sortino_ratio | -0.5180 |
| max_drawdown | 0.4596 |
| cagr | -0.2156 |
| net_avg_win | 69.1399 |
| net_avg_loss | -89.7472 |
| avg_hold_time_bars | 32.8048 |
| exposure | 0.6737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
