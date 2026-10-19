# EMA Hourly Continuation — WLD/USDT P12_26

**Symbol:** WLD/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1440 |
| net_profit_factor | 0.4954 |
| net_win_rate | 0.4465 |
| gross_profit_factor | 0.8811 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -9.1811 |
| sortino_ratio | -4.9124 |
| max_drawdown | 0.9977 |
| cagr | -0.9113 |
| net_avg_win | 15.2314 |
| net_avg_loss | -24.8067 |
| avg_hold_time_bars | 2.6313 |
| exposure | 0.1722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
