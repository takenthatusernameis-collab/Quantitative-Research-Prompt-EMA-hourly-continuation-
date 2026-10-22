# EMA Hourly Continuation — FLR/USDT P20_55

**Symbol:** FLR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1132 |
| net_profit_factor | 0.4496 |
| net_win_rate | 0.4187 |
| gross_profit_factor | 0.8863 |
| gross_win_rate | 0.4443 |
| sharpe_ratio | -9.5932 |
| sortino_ratio | -4.5528 |
| max_drawdown | 0.9968 |
| cagr | -0.8977 |
| net_avg_win | 17.1759 |
| net_avg_loss | -27.5210 |
| avg_hold_time_bars | 4.7853 |
| exposure | 0.2462 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
