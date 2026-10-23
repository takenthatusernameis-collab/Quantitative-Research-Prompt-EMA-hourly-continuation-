# EMA Hourly Continuation — REZ/USDT P34_55

**Symbol:** REZ/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 887 |
| net_profit_factor | 0.5657 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.9589 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -5.9214 |
| sortino_ratio | -2.5072 |
| max_drawdown | 0.9537 |
| cagr | -0.7036 |
| net_avg_win | 29.9770 |
| net_avg_loss | -46.1746 |
| avg_hold_time_bars | 3.8005 |
| exposure | 0.1555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
