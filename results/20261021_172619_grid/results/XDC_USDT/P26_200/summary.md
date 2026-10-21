# EMA Hourly Continuation — XDC/USDT P26_200

**Symbol:** XDC/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.7761 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 1.0155 |
| gross_win_rate | 0.5042 |
| sharpe_ratio | -1.5073 |
| sortino_ratio | -0.4053 |
| max_drawdown | 0.3824 |
| cagr | -0.1703 |
| net_avg_win | 72.8839 |
| net_avg_loss | -95.5210 |
| avg_hold_time_bars | 31.6459 |
| exposure | 0.5078 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
