# EMA Hourly Continuation — MOG/USDT P26_50

**Symbol:** MOG/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.8079 |
| net_win_rate | 0.5027 |
| gross_profit_factor | 1.0108 |
| gross_win_rate | 0.5027 |
| sharpe_ratio | -1.4170 |
| sortino_ratio | -0.4074 |
| max_drawdown | 0.3766 |
| cagr | -0.1718 |
| net_avg_win | 79.8845 |
| net_avg_loss | -99.9612 |
| avg_hold_time_bars | 6.3424 |
| exposure | 0.1160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
