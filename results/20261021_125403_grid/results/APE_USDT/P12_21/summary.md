# EMA Hourly Continuation — APE/USDT P12_21

**Symbol:** APE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 302 |
| net_profit_factor | 0.6416 |
| net_win_rate | 0.4735 |
| gross_profit_factor | 0.8977 |
| gross_win_rate | 0.4735 |
| sharpe_ratio | -2.4268 |
| sortino_ratio | -0.6033 |
| max_drawdown | 0.5095 |
| cagr | -0.2425 |
| net_avg_win | 62.8482 |
| net_avg_loss | -88.1046 |
| avg_hold_time_bars | 4.2483 |
| exposure | 0.0583 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
