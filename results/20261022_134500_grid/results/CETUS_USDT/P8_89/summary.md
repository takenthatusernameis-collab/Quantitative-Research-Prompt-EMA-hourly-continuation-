# EMA Hourly Continuation — CETUS/USDT P8_89

**Symbol:** CETUS/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.6840 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 0.9496 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -3.4226 |
| sortino_ratio | -1.2622 |
| max_drawdown | 0.7842 |
| cagr | -0.4511 |
| net_avg_win | 51.7836 |
| net_avg_loss | -69.1294 |
| avg_hold_time_bars | 21.3221 |
| exposure | 0.6590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
