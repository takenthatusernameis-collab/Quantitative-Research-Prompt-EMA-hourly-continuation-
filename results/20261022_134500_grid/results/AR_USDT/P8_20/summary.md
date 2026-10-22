# EMA Hourly Continuation — AR/USDT P8_20

**Symbol:** AR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1762 |
| net_profit_factor | 0.4104 |
| net_win_rate | 0.4274 |
| gross_profit_factor | 0.7877 |
| gross_win_rate | 0.4449 |
| sharpe_ratio | -11.8098 |
| sortino_ratio | -6.9612 |
| max_drawdown | 0.9999 |
| cagr | -0.9703 |
| net_avg_win | 9.2439 |
| net_avg_loss | -16.8079 |
| avg_hold_time_bars | 2.8042 |
| exposure | 0.2246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
