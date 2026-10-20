# EMA Hourly Continuation — GLM/USDT P8_20

**Symbol:** GLM/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1547 |
| net_profit_factor | 0.3883 |
| net_win_rate | 0.4350 |
| gross_profit_factor | 0.8755 |
| gross_win_rate | 0.4648 |
| sharpe_ratio | -11.3849 |
| sortino_ratio | -6.3359 |
| max_drawdown | 0.9997 |
| cagr | -0.9581 |
| net_avg_win | 9.4276 |
| net_avg_loss | -18.6971 |
| avg_hold_time_bars | 3.5320 |
| exposure | 0.2484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
