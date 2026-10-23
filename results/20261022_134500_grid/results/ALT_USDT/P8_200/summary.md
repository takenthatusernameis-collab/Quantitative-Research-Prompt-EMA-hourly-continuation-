# EMA Hourly Continuation — ALT/USDT P8_200

**Symbol:** ALT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.6917 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9571 |
| gross_win_rate | 0.4860 |
| sharpe_ratio | -2.6023 |
| sortino_ratio | -0.7534 |
| max_drawdown | 0.6178 |
| cagr | -0.3038 |
| net_avg_win | 65.6935 |
| net_avg_loss | -86.4908 |
| avg_hold_time_bars | 39.4766 |
| exposure | 0.7680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
