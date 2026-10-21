# EMA Hourly Continuation — INJ/USDT P12_55

**Symbol:** INJ/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.7943 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 0.9799 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -1.9838 |
| sortino_ratio | -0.7158 |
| max_drawdown | 0.6003 |
| cagr | -0.2816 |
| net_avg_win | 69.6175 |
| net_avg_loss | -84.6685 |
| avg_hold_time_bars | 11.6593 |
| exposure | 0.3376 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
