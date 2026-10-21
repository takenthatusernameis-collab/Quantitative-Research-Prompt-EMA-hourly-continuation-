# EMA Hourly Continuation — TRX/USDT P12_55

**Symbol:** TRX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.5210 |
| net_win_rate | 0.4918 |
| gross_profit_factor | 1.0136 |
| gross_win_rate | 0.5027 |
| sharpe_ratio | -5.0875 |
| sortino_ratio | -1.7276 |
| max_drawdown | 0.8704 |
| cagr | -0.5475 |
| net_avg_win | 34.9161 |
| net_avg_loss | -64.8475 |
| avg_hold_time_bars | 12.6801 |
| exposure | 0.3153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
