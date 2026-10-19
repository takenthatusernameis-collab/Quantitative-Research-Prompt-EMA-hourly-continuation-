# EMA Hourly Continuation — LTC/USDT P20_55

**Symbol:** LTC/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 994 |
| net_profit_factor | 0.3290 |
| net_win_rate | 0.4386 |
| gross_profit_factor | 0.8388 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -9.3520 |
| sortino_ratio | -4.1680 |
| max_drawdown | 0.9954 |
| cagr | -0.8818 |
| net_avg_win | 11.1906 |
| net_avg_loss | -26.5810 |
| avg_hold_time_bars | 4.5976 |
| exposure | 0.2077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
