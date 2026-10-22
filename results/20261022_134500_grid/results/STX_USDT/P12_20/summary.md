# EMA Hourly Continuation — STX/USDT P12_20

**Symbol:** STX/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1527 |
| net_profit_factor | 0.3286 |
| net_win_rate | 0.3890 |
| gross_profit_factor | 0.7510 |
| gross_win_rate | 0.4158 |
| sharpe_ratio | -14.3255 |
| sortino_ratio | -7.9822 |
| max_drawdown | 1.0000 |
| cagr | -0.9839 |
| net_avg_win | 8.2403 |
| net_avg_loss | -15.9641 |
| avg_hold_time_bars | 2.0753 |
| exposure | 0.1434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
