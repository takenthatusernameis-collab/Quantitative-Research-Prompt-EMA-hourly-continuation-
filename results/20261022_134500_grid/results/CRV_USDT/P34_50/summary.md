# EMA Hourly Continuation — CRV/USDT P34_50

**Symbol:** CRV/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 964 |
| net_profit_factor | 0.3646 |
| net_win_rate | 0.4180 |
| gross_profit_factor | 0.7793 |
| gross_win_rate | 0.4388 |
| sharpe_ratio | -9.1950 |
| sortino_ratio | -4.0619 |
| max_drawdown | 0.9939 |
| cagr | -0.8677 |
| net_avg_win | 14.1484 |
| net_avg_loss | -27.8780 |
| avg_hold_time_bars | 2.4087 |
| exposure | 0.1055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
