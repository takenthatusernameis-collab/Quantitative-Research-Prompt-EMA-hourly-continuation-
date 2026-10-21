# EMA Hourly Continuation — LISTA/USDT P12_55

**Symbol:** LISTA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 579 |
| net_profit_factor | 0.7219 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.8908 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -2.8872 |
| sortino_ratio | -1.0230 |
| max_drawdown | 0.7074 |
| cagr | -0.3764 |
| net_avg_win | 64.6829 |
| net_avg_loss | -77.2171 |
| avg_hold_time_bars | 13.3074 |
| exposure | 0.3768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
