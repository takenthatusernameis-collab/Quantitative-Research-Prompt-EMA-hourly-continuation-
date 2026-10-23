# EMA Hourly Continuation — POKT/USDT P12_55

**Symbol:** POKT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1155 |
| net_profit_factor | 0.4788 |
| net_win_rate | 0.3905 |
| gross_profit_factor | 0.8021 |
| gross_win_rate | 0.3991 |
| sharpe_ratio | -9.0704 |
| sortino_ratio | -4.3090 |
| max_drawdown | 0.9951 |
| cagr | -0.8785 |
| net_avg_win | 20.2711 |
| net_avg_loss | -27.1211 |
| avg_hold_time_bars | 7.2260 |
| exposure | 0.3777 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
