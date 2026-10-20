# EMA Hourly Continuation — CTC/USDT P12_34

**Symbol:** CTC/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1263 |
| net_profit_factor | 0.4174 |
| net_win_rate | 0.4418 |
| gross_profit_factor | 0.9205 |
| gross_win_rate | 0.4703 |
| sharpe_ratio | -9.3915 |
| sortino_ratio | -4.7062 |
| max_drawdown | 0.9974 |
| cagr | -0.9049 |
| net_avg_win | 12.8028 |
| net_avg_loss | -24.2792 |
| avg_hold_time_bars | 4.8519 |
| exposure | 0.2785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
