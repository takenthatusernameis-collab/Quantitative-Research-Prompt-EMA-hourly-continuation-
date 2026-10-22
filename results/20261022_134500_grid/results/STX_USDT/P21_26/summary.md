# EMA Hourly Continuation — STX/USDT P21_26

**Symbol:** STX/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1144 |
| net_profit_factor | 0.2532 |
| net_win_rate | 0.3785 |
| gross_profit_factor | 0.7141 |
| gross_win_rate | 0.4274 |
| sharpe_ratio | -13.2769 |
| sortino_ratio | -6.4868 |
| max_drawdown | 0.9998 |
| cagr | -0.9682 |
| net_avg_win | 7.8292 |
| net_avg_loss | -18.8303 |
| avg_hold_time_bars | 1.9528 |
| exposure | 0.1011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
