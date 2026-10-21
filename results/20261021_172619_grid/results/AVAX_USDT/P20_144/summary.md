# EMA Hourly Continuation — AVAX/USDT P20_144

**Symbol:** AVAX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7673 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.9405 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -1.8710 |
| sortino_ratio | -0.5155 |
| max_drawdown | 0.5220 |
| cagr | -0.2116 |
| net_avg_win | 83.3010 |
| net_avg_loss | -98.5884 |
| avg_hold_time_bars | 27.8556 |
| exposure | 0.4735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
