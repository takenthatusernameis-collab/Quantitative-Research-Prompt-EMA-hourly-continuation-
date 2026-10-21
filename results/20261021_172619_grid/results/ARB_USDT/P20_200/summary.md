# EMA Hourly Continuation — ARB/USDT P20_200

**Symbol:** ARB/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 236 |
| net_profit_factor | 1.0067 |
| net_win_rate | 0.5424 |
| gross_profit_factor | 1.1725 |
| gross_win_rate | 0.5424 |
| sharpe_ratio | 0.0825 |
| sortino_ratio | 0.0184 |
| max_drawdown | 0.1361 |
| cagr | 0.0033 |
| net_avg_win | 97.3932 |
| net_avg_loss | -114.6592 |
| avg_hold_time_bars | 64.5212 |
| exposure | 0.6921 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
