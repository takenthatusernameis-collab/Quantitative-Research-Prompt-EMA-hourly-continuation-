# EMA Hourly Continuation — MOVR/USDT P20_100

**Symbol:** MOVR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 772 |
| net_profit_factor | 0.5489 |
| net_win_rate | 0.4430 |
| gross_profit_factor | 0.8195 |
| gross_win_rate | 0.4534 |
| sharpe_ratio | -5.0278 |
| sortino_ratio | -1.9619 |
| max_drawdown | 0.9057 |
| cagr | -0.6067 |
| net_avg_win | 32.1598 |
| net_avg_loss | -46.6013 |
| avg_hold_time_bars | 11.4430 |
| exposure | 0.4015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
