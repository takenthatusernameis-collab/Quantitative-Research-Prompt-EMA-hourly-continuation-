# EMA Hourly Continuation — BCH/USDT P12_20

**Symbol:** BCH/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1416 |
| net_profit_factor | 0.1679 |
| net_win_rate | 0.3559 |
| gross_profit_factor | 0.6351 |
| gross_win_rate | 0.4131 |
| sharpe_ratio | -16.6690 |
| sortino_ratio | -9.2144 |
| max_drawdown | 1.0000 |
| cagr | -0.9935 |
| net_avg_win | 4.0022 |
| net_avg_loss | -13.1766 |
| avg_hold_time_bars | 2.1582 |
| exposure | 0.1389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
