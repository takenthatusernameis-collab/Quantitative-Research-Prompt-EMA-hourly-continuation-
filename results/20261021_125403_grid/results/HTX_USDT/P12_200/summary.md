# EMA Hourly Continuation — HTX/USDT P12_200

**Symbol:** HTX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.7198 |
| net_win_rate | 0.5133 |
| gross_profit_factor | 1.0952 |
| gross_win_rate | 0.5171 |
| sharpe_ratio | -1.8625 |
| sortino_ratio | -0.4302 |
| max_drawdown | 0.4983 |
| cagr | -0.1833 |
| net_avg_win | 76.1196 |
| net_avg_loss | -111.5315 |
| avg_hold_time_bars | 63.4030 |
| exposure | 0.7546 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
