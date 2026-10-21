# EMA Hourly Continuation — ONE/USDT P12_200

**Symbol:** ONE/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.7826 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.9066 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -1.3390 |
| sortino_ratio | -0.3193 |
| max_drawdown | 0.3427 |
| cagr | -0.1378 |
| net_avg_win | 83.5322 |
| net_avg_loss | -96.6405 |
| avg_hold_time_bars | 57.5177 |
| exposure | 0.7373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
