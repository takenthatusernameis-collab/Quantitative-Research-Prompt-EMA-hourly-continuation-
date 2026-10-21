# EMA Hourly Continuation — ID/USDT P12_55

**Symbol:** ID/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.6928 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.9090 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -2.8266 |
| sortino_ratio | -1.0124 |
| max_drawdown | 0.7125 |
| cagr | -0.3721 |
| net_avg_win | 51.4077 |
| net_avg_loss | -68.1345 |
| avg_hold_time_bars | 13.6019 |
| exposure | 0.3896 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
