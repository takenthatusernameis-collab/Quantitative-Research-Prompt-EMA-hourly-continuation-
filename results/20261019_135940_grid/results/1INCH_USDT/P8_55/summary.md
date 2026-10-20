# EMA Hourly Continuation — 1INCH/USDT P8_55

**Symbol:** 1INCH/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1053 |
| net_profit_factor | 0.5110 |
| net_win_rate | 0.4435 |
| gross_profit_factor | 0.8711 |
| gross_win_rate | 0.4710 |
| sharpe_ratio | -7.0836 |
| sortino_ratio | -3.2309 |
| max_drawdown | 0.9814 |
| cagr | -0.7930 |
| net_avg_win | 21.9485 |
| net_avg_loss | -34.2296 |
| avg_hold_time_bars | 10.5309 |
| exposure | 0.5040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
