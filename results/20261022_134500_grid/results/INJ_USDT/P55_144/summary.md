# EMA Hourly Continuation — INJ/USDT P55_144

**Symbol:** INJ/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.5457 |
| net_win_rate | 0.4426 |
| gross_profit_factor | 0.7874 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -4.0305 |
| sortino_ratio | -1.2333 |
| max_drawdown | 0.7770 |
| cagr | -0.4484 |
| net_avg_win | 43.9381 |
| net_avg_loss | -63.9331 |
| avg_hold_time_bars | 10.4050 |
| exposure | 0.2265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
