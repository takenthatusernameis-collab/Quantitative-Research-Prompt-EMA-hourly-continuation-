# EMA Hourly Continuation — GTC/USDT P50_200

**Symbol:** GTC/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.6851 |
| net_win_rate | 0.4625 |
| gross_profit_factor | 0.8447 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -2.0752 |
| sortino_ratio | -0.5376 |
| max_drawdown | 0.4802 |
| cagr | -0.2192 |
| net_avg_win | 65.3992 |
| net_avg_loss | -82.1244 |
| avg_hold_time_bars | 25.4354 |
| exposure | 0.3850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
