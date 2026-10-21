# EMA Hourly Continuation — FET/USDT P8_20

**Symbol:** FET/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.8154 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 1.0515 |
| gross_win_rate | 0.5126 |
| sharpe_ratio | -1.3436 |
| sortino_ratio | -0.4031 |
| max_drawdown | 0.3980 |
| cagr | -0.1698 |
| net_avg_win | 73.9464 |
| net_avg_loss | -95.3938 |
| avg_hold_time_bars | 5.0851 |
| exposure | 0.1005 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
