# EMA Hourly Continuation — ACE/USDT P12_144

**Symbol:** ACE/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.7488 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.8898 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -1.7150 |
| sortino_ratio | -0.4381 |
| max_drawdown | 0.4272 |
| cagr | -0.1832 |
| net_avg_win | 77.8698 |
| net_avg_loss | -91.9753 |
| avg_hold_time_bars | 46.8098 |
| exposure | 0.6906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
