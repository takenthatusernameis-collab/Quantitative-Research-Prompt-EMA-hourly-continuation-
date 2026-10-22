# EMA Hourly Continuation — ETHFI/USDT P8_34

**Symbol:** ETHFI/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1404 |
| net_profit_factor | 0.5629 |
| net_win_rate | 0.4338 |
| gross_profit_factor | 0.8794 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -8.2045 |
| sortino_ratio | -4.3359 |
| max_drawdown | 0.9948 |
| cagr | -0.8756 |
| net_avg_win | 21.0309 |
| net_avg_loss | -28.6221 |
| avg_hold_time_bars | 5.3426 |
| exposure | 0.3410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
