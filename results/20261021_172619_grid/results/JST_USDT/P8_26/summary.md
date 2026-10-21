# EMA Hourly Continuation — JST/USDT P8_26

**Symbol:** JST/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 750 |
| net_profit_factor | 0.5054 |
| net_win_rate | 0.5107 |
| gross_profit_factor | 1.0381 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | -5.0467 |
| sortino_ratio | -1.9922 |
| max_drawdown | 0.9018 |
| cagr | -0.5980 |
| net_avg_win | 23.9995 |
| net_avg_loss | -49.5595 |
| avg_hold_time_bars | 6.8373 |
| exposure | 0.2320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
