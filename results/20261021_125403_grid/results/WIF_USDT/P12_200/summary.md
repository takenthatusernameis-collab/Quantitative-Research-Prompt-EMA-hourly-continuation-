# EMA Hourly Continuation — WIF/USDT P12_200

**Symbol:** WIF/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.7127 |
| net_win_rate | 0.4448 |
| gross_profit_factor | 0.8057 |
| gross_win_rate | 0.4448 |
| sharpe_ratio | -1.9192 |
| sortino_ratio | -0.4681 |
| max_drawdown | 0.4260 |
| cagr | -0.1949 |
| net_avg_win | 78.2855 |
| net_avg_loss | -88.0102 |
| avg_hold_time_bars | 52.0401 |
| exposure | 0.7073 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
